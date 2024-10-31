const {createServer} = require("node:http")

const hostname = '127.0.0.1'
const port = '3000'

// create a server
const server = createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end("Hello world\n")
    console.log(req)
})

server.listen(port, hostname, () => {
    console.log(`I'm listening on ${hostname}${port}`)
})
