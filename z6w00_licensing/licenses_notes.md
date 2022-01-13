---
title: Workloads and Licensing
---

Server workloads
================

EC2 instances are most commonly used for server (rather than
interactive) workloads:

-   Network servers that listen for traffic on a port and service each
    incoming request, normally multi-threaded to permit multiple
    simultaneous clients.

-   Batch processors that process tasks asynchronously as they arrive,
    often as messages in a queue or files in a folder.

Sometimes server programs are packaged and in an operating system’s
package repository. Examples include common web, database, caching, mail
and other servers. You will also encounter custom-written programs for
solving particular business needs.

Characteristics
===============

Regardless of functional purpose, server workloads have share common
characteristics:

-   Program runs non-interactively (or can be made to do so). This
    primarily means no prompted user input, and only log information to
    the console.

-   Program doesn’t normally terminate. It will keep running
    until stopped.

-   Configuration parameters either hard-coded, supplied on command-line
    or in config file(s).

Types {#sec:server-workload-types}
=====

Compiled programs

:   written in any language for which a compiler exists on the target
    machine. Many possible original languages like C, C++,
    Golang, Haskell.

    -   Needs to be compiled for OS (Linux) and have required libraries
        statically linked or available as dynamic libraries on instance.

Bytecode-compiled programs

:   where the program is packaged by the developer and a runtime is used
    to execute it on the host. Often easiest as designed
    for portability.

    Java

    :   programs compiled to run on Java Runtime Environment (JRE). JRE
        installed from packages using yum/apt. Usually bundled as JAR
        file. Ideally should be a fat-JAR file that contains all
        required libraries.

    .net

    :   (in any supported language, often C\# or VB). Similar idea to
        Java-based programs.

Interpreted programs

:   where the source code is executed by an interpreter at runtime.
    Examples: python, JavaScript.

Licensing
=========

Even prior to the cloud’s inception, licensing has always been a very
complicated topic. On the cloud, you will have to consider the licensing
requirements for the software you use.

Ways to use software
--------------------

Binary / executable

:   formats refer to machine readable copies of software that can
    execute but do not have the accompanying source code used to
    create them.

Source code

:   refers to human-readable instructions that can be compiled before
    running, interpreted at runtime, or both.

Remote usage

:   refers to network-accessible software-as-a-service that users
    connect to remotely.

Common licensing terms
----------------------

Public domain

:   software has no restrictions attached to it. Although some software
    is public domain, most is covered by either a proprietary or a
    free license.

Proprietary

:   software is restricted and often governed by a license.

End User License Agreement (EULA)

:   governs the use of proprietary software, often subject to
    many restrictions.

Free software

:   is software licensed according to four essential freedoms:

    1.  Freedom to use

    2.  Freedom to understand/modify (meaning access to source code)

    3.  Freedom to distribute (or sell)

    4.  Freedom to distribute (or sell) modified versions.

    Note that free is in the sense of “free speech” as opposed to “free
    cookies”. Free software can be bought and sold, whilst some
    proprietary software may be available at no cost.

Permissive

:   licenses allow you to modify software and then distribute or sell
    your modified version without corresponding source code.

Copyleft

:   refers to software whose free license prohibits making modifications
    and distributing them without corresponding source code.

Open source

:   is often mistakenly taken as a synonym of free software. Whilst
    having the source code is

FLOSS

:   meaning *Free Libre Open Source Software* is a catch-all term to
    encompass non-proprietary software.

shows the common free and open source software licenses and their
relationship to each other.

![Free / libre / open source software license tree<span
data-label="fig:free-licenses"></span>](licenses){width="1.0\linewidth"}
