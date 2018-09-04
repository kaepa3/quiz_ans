@cnt=0

def change(val, coins, max)
    coin =coins.shift
    if coins.size == 0 then
        @cnt += 1 if val / coin <= max
    else
        (0..val/coin).each{|i|
            change(val -coin*i, coins.clone, max-i)
        }
    ends
end

change(1000,[500,100,50,10],15)
puts @cnt