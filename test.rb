s = 'truth, beauty, fame, stupid people'
a = s.split(',')
p a
a =  a.collect{|x| x.strip || x }
p a

p a.join('-')
