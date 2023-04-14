
## N-P plot

## ---
## Example data
data <- c(2, 1.8, 2.1, 2.4, 1.9, 2.1, 2, 1.8, 2.3, 2.2)

## Sort the data
sorted.data <- sort(data)

## Count an average order
rnk <- rank(sorted.data)

## without duplicates
j <- unique(rnk)
x <- unique(sorted.data)

## calculate alpha.j (which quantiles to count)
n <- length(data)
alpha.j <- (3 * j - 1) / (3 * n + 1)

## calculate the quantiles
q.j <- qnorm(alpha.j)


## plot
plot (x, q.j, pch = 20, ylim=range( -2, 5 ), xlab = "pozorovana hodnota", ylab = "ocekavana normalni hodnota", main = "N-P plot")

# see if it is line
model <- lm (x ~ q.j)
lines (x, model$fitted.values, col = "red")
### ---

## Q-Q plot

## ---

data <- c(2, 1.8, 2.1, 2.4, 1.9, 2.1, 2, 1.8, 2.3, 2.2)

## Sort them
sorted.data <- sort(data)

## average order
rnk <- rank(sorted.data)

## without duplicates
j <- unique(rnk)
x <- unique(sorted.data)

## alpha.j
n <- length(data)
alpha.j <- (j - 0.375) / (n + 0.25)  ## see qq formula

## quantiles of desired distribution (here I used normal)
q.j <- qnorm(alpha.j)


## plotting
plot(q.j,j,pch=20,xlab="teoreticky kvantil",ylab="pozorovany kvantil",main="Q-Q plot")

# see if straight line
model <- lm (j ~ q.j)
lines (q.j, model$fitted.values, col = "red")

## ---

## P-P plot

## ---

data <- c(2, 1.8, 2.1, 2.4, 1.9, 2.1, 2, 1.8, 2.3, 2.2)

## sort
sorted.data <- sort(data)

## avg order
rnk <- rank(sorted.data)

## without duplicates
j <- unique(rnk)
x.j <- unique(sorted.data)

## normalization
avg <- mean(x.j)
std <- sqrt( mean( x.j^2 ) - (mean(x.j))^2 )

z.j <- (x.j - avg) / std

## X is teoretical distribution
X <- pnorm( z.j )

## Y is your distribution
Y <- j / n

## See if they match
plot( X, Y )
abline( 0, 1 )
## ---
