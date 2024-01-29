isEven :: Int -> Bool
isEven n = n `mod` 2 == 0


fact :: Int->Int
fact n = foldl (*) 1 [1..n]

calcOdd n = not(even n) && n`mod`3 == 0


timesTwo :: Int-> Int
timesTwo x = x*2

double :: (Int->Int) -> [Int] -> [Int]
double f [] = [] 
double f (x:xs) = f(x) :double f xs

