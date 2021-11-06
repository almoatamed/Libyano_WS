<template>
    <v-container fluid style="height:100%; background-color:#ecf0f1;">
        <v-row style="margin-top:10%">
            <v-col class="d-flex justify-center" md="12">
                <v-img id="battery" src="../../assets/logo.svg" max-width="300"></v-img>
            </v-col>
        </v-row>
    </v-container>
</template>

<style>
@keyframes blink {
    0% {
        opacity: 1;
    }
    50% {
        opacity: 0;
    }
    100% {
        opacity: 1;
    }
}

#battery {
    -webkit-animation: blink 1.5s;
    -webkit-animation-iteration-count: 100;

    animation: blink 1.5s;
    animation-iteration-count: 100;
}


</style>