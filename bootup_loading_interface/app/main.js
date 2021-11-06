// main.js

// Modules to control application life and create native browser window
const { app, BrowserWindow } = require('electron')
const path = require('path')
const {exec} = require('child_process')
function createWindow () {
  // Create the browser window.
  const mainWindow = new BrowserWindow({
    // resizable:false, 
    backgroundColor: '#2e2c29',
    movable:false,
    minimizable:false,
    closable:false, 
    alwaysOnTop:true,
    fullscreen:true,
    frame:false,
    webPreferences:{
      scrollBounce:true,
      zoomFactor:0.8,
      // devTools:false
    },
    disableAutoHideCursor:false
    // webPreferences: {
    //   preload: path.join(__dirname, 'preload.js')
    // }
  })

  // and load the index.html of the app.
  mainWindow.loadFile('index.html')

  // Open the DevTools.
  mainWindow.webContents.openDevTools()
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
var interval_holder = null
app.whenReady().then(() => {
  createWindow()
  interval_holder = setInterval(()=>{
    exec('rosnode list',(err,stdout,stderr)=>{
      if(stdout){
        console.log(stdout.split('\n').includes('/interface_process_monitor'))
        if(stdout.split('\n').includes('/interface_process_monitor')){
          setTimeout(()=>{
            clearInterval(interval_holder)
            app.quit()
          },5000)
        }
      }
    })

  },1000)

  // app.on('activate', function () {
  //   // On macOS it's common to re-create a window in the app when the
  //   // dock icon is clicked and there are no other windows open.
  //   if (BrowserWindow.getAllWindows().length === 0) createWindow()
  // })


})

// Quit when all windows are closed, except on macOS. There, it's common
// for applications and their menu bar to stay active until the user quits
// explicitly with Cmd + Q.
app.on('window-all-closed', function () {
  clearInterval(interval_holder)
  if (process.platform !== 'darwin') app.quit()
})
