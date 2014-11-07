#install.packages("MCMCpack")
library(MCMCpack)

rdirichlet(5, 500*c(0.1,0.2,0.7)) # Tight
rdirichlet(5, c(0.1,0.2,0.7))     # Not so tight
rdirichlet(5, 0.1*c(0.1,0.2,0.7)) # Bathtub
