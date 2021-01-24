#!/bin/ruby

require 'json'
require 'stringio'

def multiples(n)
    for i in 1..10
        puts "#{n} x #{i} = #{n*i}"
    end
end

n = gets.to_i
multiples(n)
