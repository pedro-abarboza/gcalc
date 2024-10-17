<template>
	<div class="block">
		<header class="flex">
		</header>
		<div class="flex">
			<div class="flex-initial m-2 p-3 col-2">
				<SideBar />
			</div>
			<div class="card flex-initial text-center m-2 p-3 col-10">
				<Panel>
					<RouterView />
				</Panel>
			</div>
		</div>
	</div>
</template>

<script setup>
	import { RouterLink, RouterView } from 'vue-router';
	import SideBar from './components/SideBar.vue';
	import Panel from 'primevue/panel';

</script>
