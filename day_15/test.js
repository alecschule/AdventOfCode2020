var fs = require('fs');

const starting = fs.readFileSync('input.txt').toString().split(',')
var hist = new Map()
var turn = 1
for (const num of starting) {
	hist.set(parseInt(num), turn)
	turn++
}

var current = 0

while (turn !== 30000000) {
	const prev = current
	current = hist.has(current) ? turn - hist.get(current) : 0
	hist.set(prev, turn)
	turn++;
}

console.log(current)
