\documentclass{pgnotes}

\title{Scalability}

\begin{document}

\maketitle

\section{Scalability}

Scalability assesses how any service (electronic or otherwise) copes with increased or reduced demand:
\begin{itemize}
\item A cafe near a college will be busy during term but may be quieter otherwise.
\item A pub in a holiday village will experience increased demand during the summer months.
\item A takeaway near a major sports stadium will experience a peak demand on match days.
\item A ticket sales website experiences peak demands when major concerts are put on sale.
\end{itemize}
Many of these demand peaks and troughs are predictable, but some are not:
Supermarkets sold out of toilet roll when the COVID-19 crisis broke.
Beer also sold out, but Corona was left on the shelf.

When a service load increases towards \SI{100}{\percent}, externally-facing performance will degrade.

\subsection{Cloud vs data centre scaling}

\begin{description}
\item[Data centre environments] buy more hardware. Hard to justify for shorter peaks. (CapEx)
\item[Cloud environments:] can provision and de-provision resources and pay only for what you use. (OpEx)
  Responsiblity for scalability splits between us and provider and depends on the service in question.
\end{description}

\subsection{Platform services}

PaaS (e.g. S3, SNS, SQS, DynamoDB, Lambda) are scaled as needed by provider.
\begin{itemize}
\item No natural barrier at \SI{100}{\percent} capacity, unexpected high bills possible.  Must monitor.
\item Generally don't see any scaling operations - the service just expands as we use it.
\end{itemize}

\subsection{Infrastructural services}

Some IaaS like VPC, EFS also scaled as needed.
Infrastructural services (EC2, RDS) are our own responsibility to scale.
This means that we will have to identify opportunities for scaling, select the most suitable methods and automate if required.
\textbf{There is rarely a ``right answer'' when it comes to scaling.}

\newpage

\section{Patterns}

There are two key scaling methods, \autoref{fig:scaling-types}.

\autoimage{scaling_types}{Horizontal vs vertical scaling}{scaling-types}

\begin{description}
\item[Vertical (scale up)] is where individual resource units are increased / decreased in capacity to meet demand.
  \begin{itemize}
  \item Does not require architectural changes to system.
  \item Scaling operations normally require an interruption in service.
  \end{itemize}
\item[Horizontal (scale out)] is where additional resource units are added / removed from a pool to meet demand.
  \begin{itemize}
  \item Scaling operations can take place without interrupting service.
  \item Requires architectural changes to the system to accomodate.
  \end{itemize}
\end{description}

Practical: 

\begin{itemize}
\item System architecture choices will have a strong influence on ease of scaling.
\item Horizontal scaling easier if each instance independent of others.
\item Some parts of a system can't be horizontally scaled and need to be vertically scaled.
\item Easiest to scale when an application is decomposed into a number of parts/services which are then scaled appropriately according to the load on that component.
\end{itemize}

\newpage
\section{EC2 scaling}

A server machine has a number of different indicators of its performance.
These include CPU load, RAM utilisation, hard disk space and network throughput.
In this treatment we will focus on CPU \& RAM capacity.

\subsection{Before scaling}

Before scaling any system / application, we should:
\begin{enumerate}
\item address inherent bottlenecks either in code (if available) or configuration. 
\item determine if the application is primarily hitting the limits on CPU, RAM or disk/network throughput.
\item decompose system into consituent parts, which runn on separate EC2 instances.
\item consider replacing IaaS components with PaaS
\end{enumerate}

\subsection{Vertical scaling}

Vertical scaling mainly involves increasing CPU/RAM capacity of an EC2 instance:
\begin{itemize}
\item Key advantage is that it doesn't need any changes to the application or its configuration.
  Almost all applications can be vertically scaled (up to some limit).
\end{itemize}
There are a number of downsides to this traditional scaling approach: 
\begin{itemize}
\item Will involve downtime.  This might be short (minutes to an hour) on a cloud service.
\item Cannot be done easily continuously on-demand, may be paying usage fees for spare capacity.
\end{itemize}

\subsection{Horizontal scaling}

Horizontal scaling involves sharing the load among a pool of EC2 instances:
\begin{itemize}
\item Instances can be added/dropped from the pool as needed.
\item All instances must (normally) be identical. Either clone or use \texttt{cloud-init}.
\item Some form of \textit{load balancing} will be needed to divide work:
  \begin{description}
  \item[Implicit:] where the architecture itself will provide a form of load balancing.
  \item[Explicit:] where we need to add/configure load balancing components. (Possible charges!)
  \end{description}    
\end{itemize}

% \begin{figure}[htbp]
%   \centering
%   \includegraphics[width=0.5\linewidth]{scaling_with_load_balancer}
%   \caption{Scaling horizontally load balancing among a number of instances}
%   \label{fig:elb-instances-schematic}
% \end{figure}
  
Benefits of horizontal scaling:
\begin{itemize}
\item Infinite scaling possible on a practical level. 
\item Instances can be added/removed without affecting other instances.
\item Can span multiple AZ and regions for redundancy: combined scaling and high-availability.
\item Can update software across pool of instances gradually without downtime.
\end{itemize}

\newpage


\section{Simple scaling example: queue processing}

Imagine we have a batch process to run on data that is dropped into S3.
This could be facial recognition, sales analytics, auto subtitling, translation etc.
We use an S3 event to send a message to an SQS queue when a new object is added.
None of the jobs depend on any other.

On an EC2 instance, a program runs to poll the SQS queue and process the data, which takes some time for each job.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.5\linewidth]{single_worker}
  \caption{Single worker processing jobs from SQS queue}
  \label{fig:single-worker}
\end{figure}

We could easily make identical EC2 instances to share the workload, \autoref{fig:scaling-workers}.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.5\linewidth]{scaling_workers}
  \caption{EC2 instances processing jobs from SQS queue}
  \label{fig:scaling-workers}
\end{figure}



\newpage

\section{Auto scaling}

Horizontal scaling can easily be automated.
A group of EC2 VMs sharing a workload is referred to as an auto scaling group.
The group of EC2 instances is managed by an auto-scaler.

\subsection{EC2 instances}

Each EC2 VM is cloned from a master image or can be setup with cloud-init.
It is critical when using auto-scaling that the machine setup is entirely automated.


\subsection{Metrics}

The auto scaling group will use a metric, usually average CPU utilisation, to decide if it needs to add or drop instances.
But, it could be any other metric, like number of items in a queue, \autoref{fig:sqs-queue-size-scaling}.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.5\linewidth]{sqs_queue_size_scaling}
  \caption{Auto-scaling based on SQS queue size (AWS)}
  \label{fig:sqs-queue-size-scaling}
\end{figure}

These metrics are sent to Amazon CloudWatch, which generates auto-scaling events to add/destroy EC2 instances as required.


\subsection{Adding additional capacity}

When the load exceeds a threshold for a defined period of time, the autoscaler will start up a new EC2 instance by cloning an AMI and/oror using cloud-init.
There will normally be a delay before the autoscaler adds any new machines.

\subsection{Removing excess capacity}

When the average CPU loads drops below a lower threshold for a defined period of time, the autoscaler will shutdown one EC2 in the group.
This will normally send a shutdown signal to the machine, similar to pressing the power button on a PC.
The EC2 is destroyed once terminated.

\subsection{Spot instances}

Depending on the workload, scaling can use EC2 Spot Instances.
This is like NightSaver electricity, when the EC2 spot price drops as overall demand falls.

For example, we may be running analytics that don't have to be realtime.



\section{Load balancing}

EC2 instances are often used to provide network services.
To share an incoming load among a number of instances, we need to \textbf{load balance}.

\subsection{Network load balancer}

Load balancing can be done in on-site scenarios using a hardware load balancer.
This obviously isn't an option in cloud environments.

AWS provide load balancers which are actually implemented as part of AWS software-defined networking that underlies VPCs.
Although the load balancer looks like a single-point-of-failure, it's actually implemented in a distributed way through the AWS infrastructure.

\subsection{DNS-based}

A second form of load-balancing can be implemented by having multiple IP addresses for a given hostname in DNS.
This is a form of \textit{implicit} load balancing, as no additional hardware/software is needed.

\subsection{Web application example}

Simple web applications are relatively easy to scale.
We simply add more EC2 instances and load balance the traffic among them, \autoref{fig:scaling-with-load-balancer}.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.6\linewidth]{scaling_with_load_balancer}
  \caption{Scaling with load balancer}
  \label{fig:scaling-with-load-balancer}
\end{figure}

In fact, this pattern will extend to many network service applications, not just web servers.

\newpage
\section{Service scalability}

Many network services need to access other backend services, giving the pattern shown in \autoref{fig:web-single-db}.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.5\linewidth]{web_single_db}
  \caption{Load-balanced EC2 accessing database}
  \label{fig:web-single-db}
\end{figure}

\subsection{Front-end and Back-end service examples}

Back-end services might include Database, storage (S3 or EFS), message brokers, SMTP servers. 
Front-ends often seen using this pattern might include: 
\begin{itemize}
\item Web application servers (e.g. PHP / Java)
\item EC2-based SSH login servers for interactive usage (such as for data analytics, legacy UNIX terminal applications, teaching programming, business transaction processing)
\item HTTP proxy caching servers accessing single HTTP server (very common pattern)
\end{itemize}
Obviously the front-end instances are likely to be accessing several different backend services.

\subsection{Horizontal backend service scalability}

The backend service itself needs to be able to handle the increased load:
\begin{itemize}
\item AWS platform services like SNS, S3, SQS, DynamoDB, Lambda will auto-scale on demand.
  You don't have to scale them.
\item Some backend services, like SMTP servers can be simply scaled horizontally.
\item Other backend services, particularly relational databases, need special consideration to make them scale horizontally.
\end{itemize}

\newpage

\subsection{Backend service scaling}

Many backend services can themselves be horizontally scaled, \autoref{fig:backend-scaling}. 

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.6\linewidth]{backend_scaling}
  \caption{Backend scaling}
  \label{fig:backend-scaling}
\end{figure}


\newpage

\section{Relational database scaling}

In general, relational databases cannot be scaled by simply adding more instances.
Data must be available on all nodes maintaining ACID-compliance.
This limits our options to:
\begin{itemize}
\item Vertically scale the relational database.
  This will eventually hit a limit, and may incur large cost due to over-provisioning.
\item Split the relational database workload between one master server and multiple slave servers:
  \begin{itemize}
  \item Master database takes all write traffic and scales vertically.
  \item Slaves handle read-traffic and scale horizontally.
  \item Utilise built-in database replication to provide read slave replicas.
  \item
    This method will work best when the read query load greatly exceeds the write load.
    Luckily, this is the case for many applications.
  \end{itemize}
\end{itemize}

\subsection{Replication}

Replication is a feature available on most common relational database engines (MySQL, Oracle, PostgreSQL). 
A \textit{slave} follows the \textit{master} database.

\begin{description}
\item[Synchronous] replication will not return from a \texttt{COMMIT} until the transaction has been replicated to the slave DB.
\item[Asynchronous] replication will return immediately from a \texttt{COMMIT} once the transaction has been committed on the master DB as normal. The transaction will be replicated to the slave some time later. (This may be very short!)
\end{description}

We can connect to the slave database and use it as we would the master, except that:
\begin{itemize}
\item Read-only queries will proceed as normal.
\item Writes can be made only to the master. Slaves will reject them.
  \begin{itemize}
  \item Our application / system must be able to maintain two separate database connections and direct queries appropriately.
  \end{itemize}
\end{itemize}

Some database engines do in in limited circumstances permit multi-master replication.
Most will not.
For those that do, it usually breaks one of the ACID principles, and only makes sense in limited circumstances.

Control of replication depends on the database engine we're using.
Some databases have the slave initiate the replication connection to the master.
In others, the master initiates the connection to the slave.

Normally a slave can ``catch up'' if disconnected from the master for some time.
For example, if a new slave is brought online it will be able to go from no data up to being consistent with the mater.
Often however we use other methods to ``seed'' a slave with a copy of the master DB.

\newpage

\subsection{Scaling with read replicas}

\autoref{fig:db-read-replica-scaling} shows a horizontally-scaled front-end connecting to a master/slave backend service.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=1.0\linewidth]{db_read_replica_scaling}
  \caption{Horizontal scaling with read replicas}
  \label{fig:db-read-replica-scaling}
\end{figure}

Looking at the diagram:
\begin{itemize}
\item Front-end servers maintain \textit{two} database connections each: to both slave (solid line) and master DB (dotted line).
\item Traffic from front-end servers to slave DB servers is load balanced separately, but in the same way as front-end.
\item Replication traffic (dashed line) from master to slaves.
\item Master DB is scaled vertically to accomodate write traffic.
\end{itemize}

We can also have cascading replication schemes, where the master is replicated onto a slave which in turn is replicated onto other slaves.
This reduces replication traffic burden on the master.

\newpage

\section{Stateful web applications}

HTTP is primarily a stateless protocol.
Each web page (or other resource like a javascript, image or CSS) file is separately obtained by the browser:
\begin{description}
\item[Request] is sent from the browser to the web server for the given resource.
\item[Response] returns the resource (and accompanying header metadata) when requested by the client.
\end{description}
In this simple stateless model, horizontal scaling works perfectly.

\subsection{Maintaining state}

Many web applications now require a server to be able to maintain client state across multiple requests (e.g. shopping basket):
\begin{itemize}
\item This involves issuing the client a \textit{cookie} that the client then presents during subsequent requests.
\item The web server then maintains a mapping from the cookie to a server-side data structure.
\item The exact implementation of this varies depending on the server-side programming language and framework. 
\end{itemize}
Once horizontal scaling is employed, an immediate problem has the potential to develop:
How do we ensure that a client's session is maintained across multiple requests when a load balancer is employed?


\subsection{Sticky load balancing}

We can configure the load balancer to ``stick'' a particular client to a server once the initial connection has been made:
\begin{itemize}
\item This requires no application or server changes.
\item Need to tune the load balancer so that load is distributed effectively, and clients not left hanging if server fails.
\end{itemize}

In general, sticky load balancing is a very easy to setup solution.

\newpage

\subsection{Shared session state}

The alternative to sticky load balancing is maintaing a shared session state across all instances.
There are many ways we can do this, but two common methods are: 

\begin{description}
\item[In-database session] where an application already uses a database, the session data can instead be placed there.
  \begin{itemize}
  \item This will normally cause a large load on the DB server.
  \item Requires application or server configuration change (difficulty depends on specific language, framework and application server).
  \end{itemize}
\item[Shared session store] is a simple, high-performance, key-value storage server shared across all instances:
  \begin{itemize}
  \item This data doesn't need to be backed up and can be often stored in RAM only.
  \item Examples include: Redis, Memcached.
  \item Requires application or server configuration change (difficulty depends on specific language, framework and application server).
  \item Represents a potential single-point-of-failure
  \item Itself needs to be scaled, ideally as a platform service so we don't deal with the scaling ourselves.
  \end{itemize}
\end{description}

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.6\linewidth]{session_store_shared}
  \caption{Shared session store}
  \label{fig:shared-session-store}
\end{figure}

In general, I recommend using sticky load balancing first, and then trying these approaches if that doesn't suit.
For example, clients remaining logged in for a long time.

\section{Auto scaling with load balancing}

Horizontal scaling can easily be automated.
A group of EC2 VMs is referred to as an auto scaling group.
Each EC2 VM is cloned from a master image or can be setup with cloud-init. 

The auto scaling group will use a metric, usually CPU utilisation, to decide if it needs to add or drop instances.
But, it could be any other metric, like number of items in a queue.

\subsection{Adding instances}

When the load exceeds a threshold for a defined period of time, the autoscaler will:
\begin{enumerate}
\item Start up a new EC2 instance by cloning an AMI and/oror using cloud-init.
\item Wait for the new machine to start up and the required services to start. This may be time-based or function by sending requests to the machine.
\item The load balancer will be then configured to send a portion of traffic to the machine.
\item The auto scaler will wait for the average CPU load to drop as a result of the new machine for a fixed time delay period before adding more instances.
\end{enumerate}

\subsection{Removing instances}

When the average CPU loads drops below a lower threshold for a defined period of time, the autoscaler will:
\begin{enumerate}
\item Instruct the load balancer to stop sending requests to the VM that will be terminated.
\item Optinally wait until all active connections to the machine have been closed, or more usually wait for a short time delay.
\item Shutdown the VM and remove it.
\item The autoscaler will wait for the average CPU load to rise a result of removing the VM for a fixed time delay period before removing more machines.
\end{enumerate}

\end{document}

