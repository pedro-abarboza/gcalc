<template>
	<div class="flex">
		<div class="col-6">
			<Image src="src/assets/logotipos/logo-1.png" alt="Image" width="400" />
		</div>
	
		<div class="col-6 flex align-items-center justify-content-center">
			<div class="col-6">
				<InputGroup>
					<InputGroupAddon>
						<i class="pi pi-user"></i>
					</InputGroupAddon>
					<InputText placeholder="Username" type="text" v-model="usuario" />
				</InputGroup>
		
				<InputGroup>
					<InputGroupAddon><i class="pi pi-key"></i></InputGroupAddon>
					<InputText placeholder="Senha" type="password" />
				</InputGroup>
				<Button>Login</Button>
			</div>
		</div>
	</div>
</template>

<script setup>

</script>