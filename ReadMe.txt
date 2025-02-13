This project implements a simple blockchain system for secure and decentralized transaction management. It features a RESTful API to add transactions, mine blocks, and synchronize nodes. Key technologies include Python and Flask, with SHA-256 hashing for security. Clone the repository to run and test it locally.
Caution N ote that Windows does not support single quote (') when using curl in the command line. Hence, you need to use double quote and use the slash
character (\) to turn off the meaning of double quotes (") in your double-quoted
string. The preceding command in Windows would be
curl -X POST -H "Content-Type: application/json" -d "{
\"sender\": \"04d0988bfa799f7d7ef9ab3de97ef481\",
\"recipient\": \"cd0f75d2367ad456607647edde665d6f\",
\"amount\": 5}" "http://localhost:5000/transactions/new"
