# Gitlab repository setup

Assume that we are required to call our project `cloud_ca2` and we are required to add `grantp` with developer access to our project.

## Steps

1. Login to the [gitlab server](https://gitlab.comp.dkit.ie).

2. Click *New project*.

3. Click *Create blank project*.

4. For Project Name fill in `cloud_ca2`. (Name **must** match **exactly**).

5. Leave visiblity level at private.

6. Leave *Initialize repository with a README* turned on.

7. Leave SAST turned off.

8. Click *Create project*.

9. Go to *Manage* and then *Members*.

10. Add `grantp` as a Developer to your project.

11. Click the blue **Code** button and copy the HTTPS url. 

12. You can clone your project using `git clone` followed by the URL from the previous step.

