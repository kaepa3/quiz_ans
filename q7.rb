require "date"

start_date = Date.new(1964, 10 ,10)
end_date = Date.new(2020, 7 ,24)

loop do
    # 二進数に変換
    date_val = sprintf("%d%02d%02d%", start_date.year, start_date.month, start_date.day).to_i()
    date_string = date_val.to_i().to_s(2)
    # 反転
    date_string.reverse!
    # 10進数に戻す
    val = date_string.to_i(2)
    puts val if date_val == val

    start_date = start_date + 1
    break if end_date < start_date
end
