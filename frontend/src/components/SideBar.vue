<script>
import PanelMenu from 'primevue/panelmenu';
</script>

<template>
    <div class="card flex justify-center">
        <PanelMenu :model="items" class="w-full md:w-80"/>
    </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from 'vue-router';

const router = useRouter();
var lista = []

    lista.push(
    {
        label: 'Home',
        icon: 'pi pi-home',
        command: ()=>{router.push('/');}
    });

    lista.push(
    {
        label: 'Login',
        icon: 'pi pi-home',
        command: ()=>{router.push('/login');}
    });

    lista.push(
    {
        label: 'Processos',
        icon: 'pi pi-folder',
        items: [
            {
                label: 'Listagem',
                icon: 'pi pi-list',
                route: '/theming/styled'
            },
            {
                label: 'Reclamada',
                icon: 'pi pi-building',
            },
            {
                label: 'Reclamante',
                icon: 'pi pi-user',
            },
        ]
    });

    lista.push({
        label: 'Programmatic',
        icon: 'pi pi-link',
        command: () => {
            router.push('/introduction');
        }
    });

    lista.push({
        label: 'External',
        icon: 'pi pi-home',
        items: [
            {
                label: 'Vue.js',
                icon: 'pi pi-star',
                url: 'https://vuejs.org/'
            },
            {
                label: 'Vite.js',
                icon: 'pi pi-bookmark',
                url: 'https://vuejs.org/'
            }
        ]
    })

const items = ref(lista);
</script>


<style scoped>
    
</style>