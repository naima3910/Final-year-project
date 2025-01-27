// static/patientmeds/patientmeds.js

$(function() {
    $("#jsGrid").jsGrid({
        height: "80%",
        width: "100%",
        filtering: true,
        inserting: true,
        editing: true,
        sorting: true,
        paging: true,
        autoload: true,
        pageSize: 10,
        pageButtonCount: 5,
        deleteConfirm: "Do you really want to delete this medication?",
        controller: {
            loadData: function(filter) {
                var d = $.Deferred();
                $.ajax({
                    type: "GET",
                    url: "/patientmeds/api",
                    data: filter
                }).done(function(result) {
                    d.resolve($.map(result, function(item) {
                        return $.extend(item.fields, { id: item.pk });
                    }));
                });
                return d.promise();
            },
            insertItem: function(item) {
                var d = $.Deferred();
                $.ajax({
                    type: "POST",
                    url: "/patientmeds/api",
                    data: item
                }).done(function(data) {
                    $.map(data, function(item) {
                        return $.extend(item.fields, { id: item.pk });
                    });
                    d.resolve(data[0].fields);
                });
                return d.promise();
            },
            updateItem: function(item) {
                return $.ajax({
                    type: "PUT",
                    url: "/patientmeds/api/" + item.id,
                    data: item
                });
            },
            deleteItem: function(item) {
                return $.ajax({
                    type: "DELETE",
                    url: "/patientmeds/api/" + item.id
                });
            }
        },
        fields: [
            { name: "meds_name", type: "text", width: 150 },
            { name: "meds_strength", type: "text", width: 50 },
            { name: "meds_dir", type: "text", width: 50 },
            { name: "meds_status", type: "text", width: 50 },
            { name: "meds_date", type: "text", width: 50 },
            { type: "control" }
        ]
    });
});
