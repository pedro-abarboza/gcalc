<template>
    <div class="dropdown position-fixed bottom-0 end-0 mb-3 me-3 bd-mode-toggle" style="z-index:1500">
        <button class="btn btn-primary py-2 dropdown-toggle d-flex align-items-center " 
            id="bd-theme" type="button" aria-expanded="false" data-bs-toggle="dropdown" 
            aria-label="Toggle theme (dark)" >
            <span class="visually-hidden" id="bd-theme-text">Toggle theme</span>
        </button>
        <ul class="dropdown-menu dropdown-menu-end shadow" aria-labelledby="bd-theme-text" style="">
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center" data-bs-theme-value="light" aria-pressed="false">
                     Light
                </button>
            </li>
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center active" data-bs-theme-value="dark" aria-pressed="true">
                     Dark
                </button>
            </li>
            <li>
                <button type="button" class="dropdown-item d-flex align-items-center" data-bs-theme-value="auto" aria-pressed="false">
                     Auto
                </button>
            </li>
        </ul>
    </div>
    <footer class="d-flex fixed-bottom flex-wrap ps-3 justify-content-center align-items-center py-3 my-4 border-top">
        <div class="d-flex align-items-center">
            <a href="/" class="mb-3 me-2 mb-md-0 text-body-secondary text-decoration-none lh-1">
                <img alt="Vue logo" src="../assets/logotipos/pabj-logo-ss.png" style="height: 50px;">
            </a>
            <span class="mb-3 mb-md-0 text-body-secondary">© 2024 Company, Inc</span>
        </div>
    </footer>

</template>

<script>
export default {

}
</script>