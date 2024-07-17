/** @odoo-module **/
import {patch} from "@web/core/utils/patch";
import {many2OneField} from "@web/views/fields/many2one/many2one_field";
import {many2ManyTagsField} from "@web/views/fields/many2many_tags/many2many_tags_field";


patch(many2OneField, {
    extractProps({ attrs, context, decorations, options, string }, dynamicInfo) {
        var res = super.extractProps({ attrs, context, decorations, options, string }, dynamicInfo)
        res.canQuickCreate = false
        res.canCreateEdit = false
        return res
    },
});


patch(many2ManyTagsField, {
   extractProps({ attrs, context, decorations, options, string }, dynamicInfo) {
       var res = super.extractProps({ attrs, context, decorations, options, string }, dynamicInfo)
       res.canQuickCreate = false
       res.canCreateEdit = false
       return res
   }
});


