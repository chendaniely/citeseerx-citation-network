setwd("~/git/vbi/citeseerx-citation-network/citeseerx_citation_network")

library(igraph)

d <- read.csv('ouput_results.csv', header = FALSE, stringsAsFactors = FALSE)

e <- graph.edgelist(el = as.matrix(d), directed = TRUE)
e
plot(e)
