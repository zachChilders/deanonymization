# Proccessing

This is where the Spark notebooks should live.  All R scripts need to pass static analysis.  You can run `R -f validateScripts.r` to do so locally - we do it in a docker container for build validation.

Please do not run `publishnotebooks.py` outside of a check-in.  If we get into a situation where we want to test Spark stuff before check-in, its best to create a seperate, non-prod workspace.