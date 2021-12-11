<template>  
    <v-container fluid class='container d-flex align-center justify-center'>
        <div class='login grey lighten-3'>
        </div>
        <v-card elevation='17' style="opacity:0.8;"  width='400' class='pa-4'>
            <v-card-title class='text-h4'>Login</v-card-title>
            <v-card-text>
                <v-form ref="LoginForm" v-model="valid">
                    <v-row>
                        <v-col
                        cols='12'
                        >
                            <v-text-field
                            v-model="form.username"
                            type="text"
                            label="Username"
                            ></v-text-field>
                        </v-col>
                    </v-row>
                    
                    <v-row>
                        <v-col
                        cols='12'
                        >
                            <v-text-field
                            v-model="form.password"
                            label="Password"
                            type='password'
                            ></v-text-field>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col
                        cols='12'
                        >
                            <v-btn
                            large
                            block
                            color='success'
                            :rounded="true"
                            :loading='loading'
                            :disabled='loading'
                            @click='login'
                            >Login</v-btn>
                        </v-col>
                        
                    </v-row>
                </v-form>
            </v-card-text>
        </v-card>
    </v-container>
</template>

<script>
export default {
    data(){
        return{
            form:{
                username:'',
                password:''
            },
            valid:true,
            loading:false,
        }
    },
    computed:{
    },
    methods:{
        login(){
            this.loading = true
            var self = this
            this.$store.dispatch('User/login',this.form,{root:true}).then(()=>{
                self.loading = false
                if(this.$route.query['redirect']){
                    this.$router.push(this.$route.query.redirect).then(()=>{}).catch(err=>{console.log(err)})
                }else{
                    this.$router.push('/').then(()=>{}).catch(err=>{console.log(err)})
                }
            }).catch(()=>{
                self.loading = false
            })
    }
    }
}
</script>
<style  scoped>
.login{
    position:fixed;
    top:0px;
    bottom:0px;
    left:0px;
    right:0px;
    background: linear-gradient(to bottom, #68EACC 0%, #497BE8 100%);
}
.container{
    position:absolute;
    top:0px;
    bottom:0px;
    left:0px;
    right:0px;
}
</style>