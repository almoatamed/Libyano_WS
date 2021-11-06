<template>
    <v-container fluid style="height:100%; background-color:black;">
        <v-row style="margin-top:10%">
            <v-col class="d-flex justify-center" md="12">
                <v-img id="battery" src="../assets/lowbattery/battery.svg" max-width="300"></v-img>
            </v-col>
            <v-col class="d-flex justify-center" md="12">
                <v-img src="../assets/lowbattery/battery_low.svg" max-width="300"></v-img>
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
    -webkit-animation: blink 1s;
    -webkit-animation-iteration-count: infinite;
}


</style>