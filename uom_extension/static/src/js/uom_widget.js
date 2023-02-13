/* global ace */
odoo.define('uom_extension.basic_fields', function (require) {
"use strict";

var FieldFloat = require('web.basic_fields');
var registry = require('web.field_registry');
var AbstractField = require('web.AbstractField');
var basicFields = require('web.basic_fields');
var core = require('web.core');


var _lt = core._lt;

var CustomUomWidget = basicFields.FieldFloat.extend({
    description: _lt("uom_widget"),

    isQuickEditable: true,

    init: function () {
        this._super.apply(this, arguments);
        let uom = this._setDigits();
        if (typeof(uom) === "object") {
            if (['Units', 'units', 'Dozens', 'dozens'].includes(uom.data.display_name)) {
                this.formatOptions.digits = '[0, 0]';
            }
        }
        if (typeof(uom) === "string") {
            if (['Units', 'units', 'Dozens', 'dozens'].includes(uom)) {
                this.formatOptions.digits = '[0, 0]';
            }
        }
    },

    async reset() {
        await this._super(...arguments);
        if (!this.isDirty) {
            await this._render();
        }
    },

    _setDigits: function () {
        let UomField = this.nodeOptions.uom_field;
        let uom = this.record.data[UomField];
        if (!uom) {
            return false;
        }
        return uom;
    },

});

registry.add("uom_widget", CustomUomWidget);

return CustomUomWidget;

});