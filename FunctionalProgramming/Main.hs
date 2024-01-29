main = do
    putStrLn "Hello World!"

addSomething :: Int -> Int -> Int
addSomething x y = x + y

getQuadratic :: Int -> Int
getQuadratic x = x * x + 5*x + 1

circleArea :: Float -> Float
circleArea x = x * x * pi

circleDifference :: Float -> Float -> Float
circleDifference r1 r2 = abs(circleArea(r1) - circleArea(r2))

squArea :: Float -> Float
squArea x = x * x

g :: Float -> Float -> Float
g x y = 2 * x + 3 * y

sumDiff :: Float -> Float -> (Float,Float)
sumDiff a b = (a+b, abs(a-b))

farenToCels :: Float -> Float
farenToCels f = (5/9) * (f-32)

celsToFaren :: Float -> Float
celsToFaren c = c/(5/9) + 32

times  x y z = x * y * z

fiveDeep l w = times 5 l w

fib :: Int -> Int
fib 1 = 1
fib 2 = 1
fib n = fib(n-1) + fib(n-2)

fact :: Integer -> Integer
fact 1 = 1
fact n = n * fact(n-1)

isEven :: Int -> Bool
isEven n = n `mod` 2 == 0