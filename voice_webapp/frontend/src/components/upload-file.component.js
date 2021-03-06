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
      isRecorded: true,
			isBlocked: false,
      selectedFile: null,
      show_features: [],
      show_output: []
		}
	}


onFileChange = event => {
    
      // Update the state
      this.setState({ selectedFile: event.target.files[0] });
    
    };
    
    // On file upload (click the upload button)
    onFileUpload = () => {
    
      // Create an object of formData
      const formData = new FormData();

  
      var uploaded_file = this.state.selectedFile;
      uploaded_file._name = uploaded_file.name.replaceAll(" ","_");
      this.setState({uploaded_file});

      // Update the formData object
      formData.append("audio_file", this.state.selectedFile, this.state.selectedFile._name);
      formData.append("audio_name", this.state.selectedFile.name);

      // Details of the uploaded file
      console.log(this.state.selectedFile);
      console.log(this.state.selectedFile._name);
    
      // Request made to the backend api
      // Send formData object
      let url = 'http://localhost:8000/api/audiofiles/';
      var path = require("path");
      axios.post(url, formData, {
      headers: {
        'content-type': 'multipart/form-data'
      }
    })
        .then(res => {
          this.setState({blobURL: "http://localhost:8000" + res.data.audio_file});
          this.setState({isRecorded: false});
          console.log(res.data);
        })
        .catch(err => console.log(err))

    };

    // On file upload (click the upload button)
    doFeatureExtraction = () => {
    
      // Create an object of formData
      const formData = new FormData();
    
      // Update the formData object
      formData.append("file_details", this.state.selectedFile, this.state.selectedFile._name);
      formData.append("file_name", this.state.selectedFile._name);

      // Details of the uploaded file
      console.log(this.state.selectedFile);
      console.log(this.state.selectedFile._name);
    
      // Request made to the backend api
      // Send formData object
      let url = 'http://localhost:8000/api/disorder_detection/';

      axios.post(url, formData, {
      headers: {
        'content-type': 'multipart/form-data'
      }
    })
        .then(res => {
            this.setState({show_features: res.data.features});
            this.setState({show_output: res.data.output});
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
                    <button onClick={this.onFileUpload} disabled = {this.state.selectedFile == null}>
                    Upload
                    </button>
                    
                    <button onClick={this.doFeatureExtraction} disabled = {this.state.isRecorded}>
                    Run Model
                    </button>
                </div>

                {this.fileData()}
                <audio src={this.state.blobURL} controls="controls" />
                <div> {this.state.show_output} </div>
                </div>
              )
    }
}
