<template>
    <header class="d-flex justify-content-between p-2 py-md-4 border-bottom sombra align-items-center">
        <div class="offcanvas-lg">
            <img alt="Vue logo" src="../assets/logotipos/logo-text-1.png" style="height: 60px;">
        </div>
        <div class="navbar-expand-lg">
            <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" 
                data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar" aria-label="Toggle navigation">
                <img alt="Vue logo" src="../assets/logotipos/logo-p-1.png" style="height: 60px;">
            </button>
        </div>
        <div>
            <button class="btn btn-outline-secondary me-2" data-bs-toggle="dropdown"
                style="border-radius: 50px;width: 45px;font-size: 20px;height: 45px;">
                
            </button>
            <ul class="dropdown-menu">
               
                <li class="dropdown-item nav-item">
                    <RouterLink class="nav-link" activeClass="active" to="/">
                        Home
                    </RouterLink>
                </li>
                <li class="dropdown-item nav-item">
                    <RouterLink class="nav-link" activeClass="active" to="/login">
                        Login
                    </RouterLink>
                </li>
            </ul>
        </div>
        
    </header>
</template>

<script>

export default {
}
</script>
