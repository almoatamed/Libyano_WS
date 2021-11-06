<template>
    <v-container fluid style="height:100%; background-color:black;">
        <v-row style="margin-top:10%">
            <v-col class="d-flex justify-center" md="12">
                <v-img id="compass" src="../assets/map/compass.svg" max-width="300"></v-img>
            </v-col>

        </v-row>
    </v-container>
</template>

<style>
@-moz-keyframes spin { 
    100% { -moz-transform: rotate(360deg); } 
}
@-webkit-keyframes spin { 
    100% { -webkit-transform: rotate(360deg); } 
}
@keyframes spin { 
    100% { 
        -webkit-transform: rotate(360deg); 
        transform:rotate(360deg); 
    }
} 

#compass {
    -webkit-animation:spin 6s linear infinite;
    -moz-animation:spin 6s linear infinite;
    animation:spin 6s linear infinite;
}


</style>