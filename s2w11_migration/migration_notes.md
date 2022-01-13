---
title: Migration
---

Cloud utilisation
=================

System
------

Systems of interest can be quite varied. Remember that not all systems
are 3-tier web or MS-AD environments - there is a huge world out there!
Some of the most interesting systems are the less usual!

Provision models
----------------

On-site

:   using data centre environment (of varying quality).

Co-lo

:   in a dedicated data centre facility.

Cloud

:   using 1 or more cloud providers. (Cloud provider as per Nist
    definition of cloud computing)

Pull factors
------------

1.  Replacement of capital expenditure by operational expenditure.

2.  Avoiding sunk hardware costs and upgrade cycles.

Push factors
------------

1.  Cost of maintaining on-site data centre environments and their
    supporting infrastructure (e.g. power, cooling,
    monitoring, networking).

2.  Demand for space / reduced rental costs

Candidate systems
=================

Important to consider what can be moved vs what should be moved.

System decomposition
--------------------

System needs to be broken down into its constituent components. It is
best to consider cloud migration as a possibility for individual
components of an application, rather than the system itself as a unit.

Strategies
----------

We assume our *source environment* is the setup we are currently using.
AWS have identified [7
Rs](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-replatforming-cots-applications/apg-gloss.html)
describing different migration strategies:

Retire:

:   decommission / remove applications that are no longer needed in your
    source environment.

Retain:

:   source environment. Candidates:

    -   Applications requiring major refactoring, and you want to
        postpone that work until a later time.

    -   May be legacy applications without business justification for
        migrating them.

Repurchase / replace (drop and shop)

:   switch to a different product (move from custom / COTS to
    SaaS model). Example: Migrate your customer relationship
    management (CRM) system to Salesforce.com.

Rehost (lift and shift)

:   move application cloud without making changes. Example: Migrate
    on-premises database / server stack from onsite server to an EC2
    instance in the AWS Cloud.

Relocate (hypervisor-level rehost)

:   extension of the rehost model where an already virtualised
    environment is relocated to the cloud.

Replatform (lift and reshape):

:   move an application to the cloud, replacing some components with
    cloud-based equivalents. Example: Migrate your on-premises Oracle
    database to Amazon Relational Database Service (Amazon RDS) for
    Oracle in the AWS Cloud.

Refactor/re-architect:

:   modify architecture to use cloud-native capabilities. Example:
    Migrate your on-premises Oracle database to the Amazon Aurora
    PostgreSQL-Compatible Edition.

Moving any particular system will may not be a single choice.

Contra-indications
------------------

Some components present extreme difficulties (not insurmountable)
migrating to cloud environments:

1.  Non-PC/ARM based systems.

2.  **Mainframe** systems (e.g. IBM z/OS) and so-called *midrange* (e.g.
    IBM i) systems.

3.  **Legacy PC operating systems** (e.g. OS/2, Xenix, PICK, DOS),
    particularly early versions without TCP/IP support.

4.  Systems requiring **access to hardware** (e.g. serial, parallel,
    specific interface cards)

5.  Systems that **cannot function off-line** in the absense of
    connectivity (e.g. some business-critical systems)

May still be possible to move certain components of systems containing
the above to cloud environments if the system can be clearly decomposed
into interconnecting parts.

Onsite connectivity
-------------------

Moving

Possible to connect a VPC to an onsite LAN using a VPN gateway.

Some co-lo data centres offer Amazon Direct Connect (not discussed in
detail here).
