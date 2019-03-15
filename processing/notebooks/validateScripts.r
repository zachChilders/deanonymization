options(warn = 2) # Warning as error
library(lintr)
scripts <- list.files(pattern=".r$")

for (script in scripts) {
    lint(script)
}

