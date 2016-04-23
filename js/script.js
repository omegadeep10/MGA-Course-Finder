var options = {
    valueNames: ["crn", "ptrm", "subject", "number", "section", "hours", "building", "room", "title", "instructor", "time", "campus", "days", "seats"],
    page: 50,
    plugins: [ 
    ListPagination({
        paginationClass: "pagination"
    }) ]
};

var userList = new List('course-data', options);