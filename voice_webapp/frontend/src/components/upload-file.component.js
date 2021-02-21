import React, {Component} from 'react';
import axios from 'axios';
import MicRecorder from 'mic-recorder-to-mp3';
const Mp3Recorder = new MicRecorder({ bitRate: 128 });

export default class UploadFileSystem extends Component {

	constructor(props) {
		super(props);

		this.state = {
			isRecording: false,
			blobURL: '',
			isBlocked: false,
            selectedFile: null
		}
	}

    start = () => {
        if (this.state.isBlocked) {
            console.log('Permission Denied');
        } else {
            Mp3Recorder
                .start()
                .then(() => {
                    this.setState({ isRecording: true });
                }).catch((e) => console.error(e));
        }
    };

    stop = () => {
        Mp3Recorder
            .stop()
            .getMp3()
            .then(([buffer, blob]) => {
                const blobURL = URL.createObjectURL(blob)
                    console.log(blobURL);
                   this.setState({ blobURL, isRecording: false });
            }).catch((e) => console.log(e));
    };
   
onFileChange = event => {
    
      // Update the state
      this.setState({ selectedFile: event.target.files[0] });
    
    };
    
    // On file upload (click the upload button)
    onFileUpload = () => {
    
      // Create an object of formData
      const formData = new FormData();
    
      // Update the formData object
      formData.append("audio_name", this.state.selectedFile.name);
      console.log(typeof(this.state.selectedFile.name));

      // Details of the uploaded file
      console.log(this.state.selectedFile);
      console.log(this.state.selectedFile.name);
    
      // Request made to the backend api
      // Send formData object
      let url = 'http://localhost:8000/api/audiofiles/';

      axios.post(url, formData, {
      headers: {
        'content-type': 'multipart/form-data'
      }
    })
        .then(res => {
            console.log("HELLO");
          console.log(res.data);
        })
        .catch(err => console.log(err))

    };
    
    // File content to be displayed after
    // file upload is complete
    fileData = () => {
    
      if (this.state.selectedFile) {
         
        return (
          <div>
            <h2>File Details:</h2>
             
<p>File Name: {this.state.selectedFile.name}</p>
 
             
<p>File Type: {this.state.selectedFile.type}</p>
 
             
<p>
              Last Modified:{" "}
              {this.state.selectedFile.lastModifiedDate.toDateString()}
            </p>
 
          </div>
        );
      } else {
        return (
          <div>
            <br />
            <h4>Choose before Pressing the Upload button</h4>
          </div>
        );
      }
    };

    render() {
        return(
                <div>
                <h3> Upload your file </h3>
                <div>
                    <input type="file" onChange={this.onFileChange} />
                    <button onClick={this.onFileUpload}>
                    Upload
                    </button>
                </div>

                {this.fileData()}
                <audio src={this.state.blobURL} controls="controls" />
                </div>
              )
    }
}
