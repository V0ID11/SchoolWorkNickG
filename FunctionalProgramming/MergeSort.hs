lefthalf :: [Int] -> [Int]
lefthalf xs = take(length xs `div` 2) xs

righthalf :: [Int] -> [Int]
righthalf xs = drop(length xs `div` 2) xs

merge :: [Int] -> [Int] -> [Int]
merge xs [] = xs
merge [] [] = []
merge [] ys = ys

merge (x:xs) (y:ys)
    | x<y = x: merge xs (y:ys)
    | x>y = y:merge ys (x:xs)
    | x==y = x:y:merge xs ys


mergeSort :: [Int] -> [Int]
mergeSort n
    | length n == 1 = n
mergeSort n = merge (mergeSort(lefthalf (n))) (mergeSort (righthalf (n)))