---
subtitle: CloudFront
title: Content Delivery Networks
---

<span>CloudFront lab</span>

1.  Set up a CloudFront distribution that points to an S3 origin. Use
    sample website from previous S3 lab as content. Confirm that
    caching works.

2.  Write script that:

    -   Syncs folder on PC to S3 bucket

    -   Invalidates the CloudFront distribution

    Show that this works by making a change locally, rerunning script
    and viewing public URL after a short delay.
