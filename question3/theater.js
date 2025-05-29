const seats = new Array(20).fill(false);
const queue = [];
const hall = [];

function reserveSeat(num) {
    if (num >= 0 && num < seats.length) {
        if (!seats[num]) {
            seats[num] = true;
            console.log(`Seat ${num} reserved.`);
        } else {
            console.log("Seat already booked.");
        }
    } else {
        console.log("Invalid seat number.");
    }
}

function enter(name, time) {
    const limit = time === "peak" ? 5 : 10;
    if (queue.length < limit) {
        queue.push(name);
        console.log(`${name} added to queue.`);
    } else {
        console.log("Queue full!");
    }
}

function admit() {
    if (queue.length > 0) {
        const person = queue.shift();
        hall.push(person);
        console.log(`${person} entered the hall.`);
    } else {
        console.log("Queue empty.");
    }
}

function exitHall(name) {
    const index = hall.indexOf(name);
    if (index !== -1) {
        hall.splice(index, 1);
        console.log(`${name} exited.`);
    } else {
        console.log(`${name} not in hall.`);
    }
}

// Example usage
reserveSeat(4);
enter("Joshua", "peak");
admit();
exitHall("Joshua");
