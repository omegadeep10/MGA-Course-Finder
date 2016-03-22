var options = {
    valueNames: ["crn", "ptrm", "subject", "number", "section", "campus", "title", "seats", "hours", "begin", "end", "building", "room", "days", "instructor"],
    page: 50,
    plugins: [ ListPagination({
        paginationClass: "pagination"
    }) ]
};

var userList = new List('course-data', options);