n = gets.chomp.to_i
for i in 0..n-1
    s = gets.chomp
    len_ = s.length
    
    for i in 0..len_
        if i%2 == 0
            print s[i]
        end
    end
    print ' '
    for i in 1..len_
        if i%2 != 0
            print s[i]
        end
    end
    STDOUT.flush
    puts

end
