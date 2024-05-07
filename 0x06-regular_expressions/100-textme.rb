#!/usr/bin/env ruby
from_M = ARGV[0].scan(/from:(\+?\w+)/).join
to_M = ARGV[0].scan(/to:(\+?\d+)/).join
flags_M = ARGV[0].scan(/flags:([-?[0-1]:]+)/).join
puts "#{from_M},#{to_M},#{flags_M}"
