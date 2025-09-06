understanding how a flow of request from client side from a website happen and fulfill request
https://chatgpt.com/
this is a link which consist of many parts 
1- https: this means hyper text transfer protocol s for secure connection
2- chatgpt.com is a name of ip address from domain name system dns let's say its ip is 167.511.0.1
3- next part is ports ports are like workstations in a computer maximum 65535 different type of applications work on specific type of ports but one at a time in this url port number is hiden let's us say 8000. At this point this is called base url.
4- now here come routes when a request goes to specific ip address at their port then fast api determine which function need to call by matching route names https://chatgpt.com/c here c is the route or function that need to be called.https://chatgpt.com/ only / at the end means start point home of the application.
5- one more hiden thing is the request method fastapi check which method in request is. 
6- base on the request required function is called and response is send back.


Understanding ports in detail:

A port is like a door (or workstation, as you said) on a computer.

Each port is identified by a number (0–65535).

An IP address is like the street address of a building, and the port is like the door number inside that building.

For example:

If you go to 192.168.1.10:80 → you’re entering the house at address 192.168.1.10, door 80, which is usually for HTTP (web traffic).

If you go to 192.168.1.10:22 → same house, but now you enter through door 22, which is usually for SSH (remote login).

👉 Important points:

A port can only be used by one application at a time. For example, if one web server is already listening on port 8000, another can’t use the same port on that machine unless the first one is stopped.

Different applications use different ports to separate traffic (like workstations handling different tasks).

Some ports are well-known:

80 → HTTP

443 → HTTPS

22 → SSH

25 → SMTP (email)

So in our case, when you run FastAPI with uvicorn main:app --reload, it starts listening on port 8000 by default. That’s why you open http://127.0.0.1:8000/ in the browser to talk to your API.






Table of status codes



| Code                          | Meaning                       | When to Use                  | Example                        |
| ----------------------------- | ----------------------------- | ---------------------------- | ------------------------------ |
| **200 OK**                    | Request succeeded             | Successful GET, PUT, DELETE  | Fetching a user’s profile      |
| **201 Created**               | Resource created              | After POST creates something | New user registered            |
| **204 No Content**            | Success but no data returned  | DELETE or empty success      | Deleting a user                |
| **400 Bad Request**           | Invalid input                 | Missing/invalid parameters   | User submits wrong data        |
| **401 Unauthorized**          | No/invalid auth credentials   | User not logged in           | API requires login token       |
| **403 Forbidden**             | Authenticated but not allowed | No permission                | Normal user trying admin route |
| **404 Not Found**             | Resource doesn’t exist        | Invalid ID / wrong URL       | User with ID 10 not in DB      |
| **409 Conflict**              | Resource already exists       | Duplicate entry              | Username already taken         |
| **422 Unprocessable Entity**  | Validation failed             | Wrong data type              | Sending string instead of int  |
| **500 Internal Server Error** | Server-side error             | Unhandled exception          | Bug in code or DB crash        |
| **503 Service Unavailable**   | Server down / overloaded      | Maintenance mode             | API temporarily offline        |
