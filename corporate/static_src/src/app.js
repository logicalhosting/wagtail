import {MDCTopAppBar} from '@material/top-app-bar';
import {MDCDrawer} from "@material/drawer";
import {MDCCheckbox} from '@material/checkbox';
import {MDCChipSet} from '@material/chips/chip-set';
import {MDCDataTable} from '@material/data-table';
import {MDCFormField} from '@material/form-field';
import {MDCList} from "@material/list";
import {MDCRadio} from '@material/radio';
import {MDCRipple} from '@material/ripple';
import {MDCTextField} from '@material/textfield';

const topAppBar = new MDCTopAppBar.attachTo(document.querySelector('.mdc-top-app-bar'));
const drawer = new MDCDrawer.attachTo(document.querySelector('.mdc-drawer'));

topAppBar.listen('MDCTopAppBar:nav', () => {
  drawer.open = !drawer.open;
});

const dataTable = new MDCDataTable(document.querySelectorAll('.mdc-data-table'));

const selector = '.mdc-button, .mdc-icon-button, .mdc-card__primary-action';

const textField = new MDCTextField(document.querySelector('.mdc-text-field'));

const list = MDCList.attachTo(document.querySelector('.mdc-list'));
list.wrapFocus = true;

const ripples = [].map.call(document.querySelectorAll(selector), function(el) {
  return new MDCRipple(el);
});

const radio = new MDCRadio(document.querySelector('.mdc-radio'));
const formField = new MDCFormField(document.querySelector('.mdc-form-field'));
formField.input = radio;

const checkbox = new MDCCheckbox(document.querySelector('.mdc-checkbox'));
formField.input = checkbox;

const chipSetEl = document.querySelector('.mdc-chip-set');
const chipSet = new MDCChipSet(chipSetEl);

