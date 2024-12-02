console.log("ddddddddddddddddddd");

/*odoo.define('travel_package_master.test', function (require) {
    "use strict";
    console.log("eeeeeeeeeeeeeeeeeeee");
    var core = require('web.core');
    var form_common = require('web.form_common');
    var _t = core._t;
    console.log("ssssssssssssssssssss");
    form_common.FormController.include({
        on_button_click: function (event) {
            var self = this;
            if (event.data.attrs.name === 'entry_reject') { // Replace 'your_button_name' with the actual name of your button
                var rejectRemarkField = this.model.get(this.handle, {fieldNames: ['reject_remark']}).data.reject_remark;
                if (!rejectRemarkField) {
                    this.do_warn(_t('Validation Error'), _t('Enter remarks'));
                } else {
                    this._super.apply(this, arguments);
                }
            } else {
                this._super.apply(this, arguments);
            }
        },
    });
});
*/

odoo.define('travel_management.widgets', function (require) {
    'use strict';

    var FieldDate = require('web.basic_fields').FieldDate;
	console.log('ddddddddddddd');
    var YourCustomWidget = FieldDate.extend({
        init: function (parent, name, record, options) {
            this._super.apply(this, arguments);
        },
        _render: function () {
            this._super.apply(this, arguments);
            // Add your custom logic here to hide the date field based on your conditions
            // For example, check if the date is within the next 10 days and hide accordingly
              // Get the current date
            var currentDate = new Date();

            // Get the date value from the field
            var fieldValue = this.value;

            // Parse the date value
            var fieldDate = fieldValue ? new Date(fieldValue) : null;

            // Check if the date is in the past or more than 10 days in the future
            if (fieldDate && fieldDate < currentDate || (fieldDate && fieldDate > new Date(currentDate.getTime() + 10 * 24 * 60 * 60 * 1000))) {
                // Hide the date field
                this.$el.hide();
            } else {
                // Show the date field
                this.$el.show();
            }
            console.log("rrrrrrrrrrrrrrrrrrrr");
        },
    });

    // Register your custom widget using the prototype
    FieldDate.include({
        'your_custom_widget': YourCustomWidget,
    });

    return YourCustomWidget;
});


