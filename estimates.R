
## If sample mean and variance is known
## ---
confidence.interval <- function( n, sample.mean, std, alpha )
{
    quantile <- qnorm( 1 - alpha/2 )
    return
    (
      list
      (
        lower=sample.mean - quantile * std / sqrt( n ),
        upper=sample.mean + quantile * std / sqrt( n )
      )
    )
}

lower.estimate <- function( n, sample.mean, std, alpha )
{
  quantile <- qnorm( 1 - alpha )
  return( sample.mean - quantile * std / sqrt( n ) )
}

upper.estimate <- function( n, sample.mean, std, alpha )
{
  quantile <- qnorm( 1 - alpha )
  return( sample.mean + quantile * std / sqrt( n ) )
}
## ---

## mean and var are unknown --> student t distribution
## ---

## a) we want to know mean
t.mean.confidence.interval <- function( n, sample.mean, sample.std, alpha )
{
  quantile <- qt( 1 - alpha/2, df=n - 1 )
  return
  (
    list
    (
      lower=sample.mean - quantile * sample.std / sqrt( n ),
      upper=sample.mean + quantile * sample.std / sqrt( n )
    )
  )
}

t.mean.lower.estimate <- function( n, sample.mean, sample.std, alpha )
{
  quantile <- qt( 1 - alpha, df=n - 1 )
  return( sample.mean - quantile * sample.std / sqrt(n) )
}

t.mean.upper.estimate <- function( n, sample.mean, sample.std, alpha )
{
  quantile <- qt( 1 - alpha, df=n - 1 )
  return( sample.mean + quantile * sample.std / sqrt(n) )
}

## b) we want to know the variance

t.var.confidence.interval <- function( n, sample.std, alpha )
{
  quantile.1 <- qchisq( 1 - alpha/2, df=n - 1 )
  quantile.2 <- qchisq( alpha/2, df=n - 1 )
  return
  (
    list
    (
      lower=( ( n - 1 ) * sample.std^2 ) / quantile.1,
      upper=( ( n - 1 ) * sample.std^2 ) / quantile.2
    )
  )

}

t.var.lower.estimate <- function( n, sample.std, alpha )
{
  quantile <- qchisq( 1 - alpha, df=n - 1 )
  return( ( ( n - 1 ) * sample.std^2 ) / quantile )
}

t.var.upper.estimate <- function( n, sample.std, alpha )
{
  quantile <- qchisq( alpha, df=n - 1 )
  return( ( ( n - 1 ) * sample.std^2 ) / quantile )
}

## ---

## --- Example

flour <- c( 987, 1001, 993, 994, 993, 1005, 1007, 999, 995, 1002 )
sample.mean <- mean( flour )
sample.std <- sqrt( var( flour ) )
n <- length( flour )

mean.interval <- t.mean.confidence.interval(n, sample.mean, sample.std, 0.05)
var.interval <- t.var.confidence.interval(n, sample.std, 0.05)
## ---


# --- If we have TWO random selections and want to know mean.1 - mean.2
## --- if we know variances of both

double.confidence.interval <- function( n.1, n.2, sample.mean.1, sample.mean.2, std.1, std.2, alpha )
{
  
  quantile <- qnorm( 1 - alpha/2 )
  fraction.1 <- (std.1^2) / n.1
  fraction.2 <- (std.2^2) / n.2
  
  return
  (
    list
    (
      lower=sample.mean.1 - sample.mean.2 - quantile * sqrt( fraction.1 + fraction.2 ),
      upper=sample.mean.1 - sample.mean.2 + quantile * sqrt( fraction.1 + fraction.2 )
    )
  )
}

## if we do not know variances but we know they are the same

t.double.confidence.interval <- function( n.1, n.2, sample.mean.1, sample.mean.2, sample.std.1, sample.std.2, alpha )
{
  
  quantile <- qt( 1 - alpha/2, df=n.1 + n.2 - 2 )
  fraction <- ( n.1 + n.2 ) / ( n.1 * n.2 )
  
  s.12.square <- ( ( n.1 - 1 ) * ( sample.std.1^2 ) + ( n.2 - 1 ) * ( sample.std.2^2 ) ) / ( n.1 + n.2 - 2 )
  
  return
  (
    list
    (
      lower=sample.mean.1 - sample.mean.2 - quantile * sqrt( s.12.square ) * sqrt(fraction),
      upper=sample.mean.1 - sample.mean.2 + quantile * sqrt( s.12.square ) * sqrt(fraction)
    )
  )
}
# ---

## --- Example

A <- c(62, 54, 55, 60, 53, 58)
B <- c(52, 56, 50, 49, 51)

n.1 <- length( A )
n.2 <- length( B )
sample.mean.1 <- mean( A )
sample.mean.2 <- mean( B )
sample.std.1 <- sqrt( var( A ) )
sample.std.2 <- sqrt( var( B ) )

t.double.confidence.interval( n.1, n.2, sample.mean.1, sample.mean.2, sample.std.1, sample.std.2, 0.05 )
## ---

## --- If we do not know the variances and want to know they ratio ( this is v1^2 / v2^2)

f.squared.double.confidence.interval <- function(n.1, n.2, sample.std.1, samle.std.2, alpha )
{
  
  quantile.1 <- qf( 1 - alpha/2, df1=n.1-1, df2=n.2-1 )
  quantile.2 <- qf( alpha/2, df1=n.1-1, df2=n.2-1 )
  
  return
  (
    list
    (
      lower=(sample.std.1^2 / sample.std.2^2) * (1 / quantile.1),
      upper=(sample.std.1^2 / sample.std.2^2) * (1 / quantile.2)
    )
  )
}
## ---


## --- Example

## TODO

sample.std.1 <- 0.0058
sample.std.2 <- 0.028

f.squared.double.confidence.interval( 4, 4, sample.std.1, sample.std.2, 0.05 )

