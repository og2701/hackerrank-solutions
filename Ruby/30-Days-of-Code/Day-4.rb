class Person
    attr_accessor :age
    def initialize(initialAge)
        @age = 0
        if initialAge < 0
            puts "Age is not valid, setting age to 0.\n"
        else
            @age = initialAge
        end 
    end
    def amIOld()
        if age < 13
            puts "You are young.\n"
        else if age >= 13 and age < 18
            puts "You are a teenager.\n"
        else
            puts "You are old.\n"
        end
    end
    def yearPasses()
        @age += 1
    end
end
end
T=gets.to_i
for i in (1..T)do
    age=gets.to_i
    p=Person.new(age)
    p.amIOld()
    for j in (1..3)do
        p.yearPasses()
    end
    p.amIOld
  	puts ""
end      
