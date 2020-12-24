#!/bin/ruby

require 'json'
require 'stringio'


def solve(meal_cost, tip_percent, tax_percent)
    puts (meal_cost * (1+(tip_percent.to_f+tax_percent.to_f)/100)).round()

end

meal_cost = gets.to_f

tip_percent = gets.to_i

tax_percent = gets.to_i

solve meal_cost, tip_percent, tax_percent
