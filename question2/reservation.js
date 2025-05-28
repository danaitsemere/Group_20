class Reservation {
    constructor(guest, room, checkIn, checkOut) {
        this.guest = guest;
        this.room = room;
        this.checkIn = new Date(checkIn);
        this.checkOut = new Date(checkOut);
        this.paid = false;
        this.checkedIn = false;
    }
}

class Hotel {
    constructor(rooms) {
        this.rooms = rooms;
        this.reservations = [];
    }

    isAvailable(room, checkIn, checkOut) {
        const checkInDate = new Date(checkIn);
        const checkOutDate = new Date(checkOut);
        return !this.reservations.some(res =>
            res.room === room &&
            !(checkOutDate <= res.checkIn || checkInDate >= res.checkOut)
        );
    }

    bookRoom(guest, room, checkIn, checkOut) {
        if (!this.rooms.includes(room)) {
            console.log(`Room ${room} does not exist.`);
            return;
        }
        if (this.isAvailable(room, checkIn, checkOut)) {
            const reservation = new Reservation(guest, room, checkIn, checkOut);
            this.reservations.push(reservation);
            console.log(`Room ${room} booked for ${guest} from ${checkIn} to ${checkOut}.`);
        } else {
            console.log(`Room ${room} is not available from ${checkIn} to ${checkOut}.`);
        }
    }

    checkIn(guest) {
        const reservation = this.reservations.find(res => res.guest === guest && !res.checkedIn);
        if (reservation) {
            reservation.checkedIn = true;
            console.log(`${guest} has checked into room ${reservation.room}.`);
        } else {
            console.log(`No reservation found for ${guest}.`);
        }
    }

    processPayment(guest) {
        const reservation = this.reservations.find(res => res.guest === guest && !res.paid);
        if (reservation) {
            reservation.paid = true;
            console.log(`Payment processed for ${guest}.`);
        } else {
            console.log(`No unpaid reservation found for ${guest}.`);
        }
    }
}


const hotel = new Hotel([101, 102, 103]);
hotel.bookRoom("Qefar", 101, "2025-05-20", "2025-05-22");
hotel.bookRoom("Khalid", 101, "2025-05-21", "2025-05-23"); // Overlaps with Alice
hotel.checkIn("Qefar");
hotel.processPayment("Qefar");
