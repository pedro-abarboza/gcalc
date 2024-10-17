import './assets/main.css';

import { createApp } from 'vue';
import { createPinia } from 'pinia';

import App from './App.vue';
import router from './router';

import PrimeVue from 'primevue/config';
import Aura from '@primevue/themes/aura';

import Button from "primevue/button"
import Image from 'primevue/image';

import InputText from 'primevue/inputtext';
import InputNumber from 'primevue/inputnumber';

import InputGroup from 'primevue/inputgroup';
import InputGroupAddon from 'primevue/inputgroupaddon';

const app = createApp(App)
app.use(PrimeVue, {
    theme: {
        preset: Aura,
    },
});
app.component('Button', Button);
app.component('Image', Image);

app.component('InputText', InputText);
app.component('InputNumber', InputNumber);

app.component('InputGroup', InputGroup);
app.component('InputGroupAddon', InputGroupAddon);

app.use(createPinia())
app.use(router)

app.mount('#app')
