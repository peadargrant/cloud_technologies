\documentclass{article}

\begin{document}

This section looks at applying the ideas of vertical and (particularly) horizontal scaling to network services.
We often think of web applications, but many other network services can be scaled in this manner.
Some can't.

Many of our network services are split between a front-end that actually provides the service, and various backend(s) that are accessed by the front-end.
Backend services sometimes are PaaS-type services like SQS, SNS, S3 but other times they are custom applications running on cloud infrastructure.
Often we want to scale both the front-end and back-end as needed.

Relational Databases are a particular problem for scaling, because their ACID-compliance precludes some simpler scaling ideas.
We look at the ways they can be scaled in spite of these issues. 

\begin{enumerate}

\item
  \textbf{Read the notes} on service scalability.

\item
  \textbf{Reflect back} on a project or CA you did where a number of services interacted.
  Draw a diagram of the service as originally designed.
  Then, on a separate diagram or overlaid on the original, show how the consituent parts could scale.

\end{enumerate}

\end{document}
