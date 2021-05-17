import React, { Component } from 'react';
import SurfSpotService from './SurfSpotService'
const surfspotService = new SurfSpotService();

class SurfSpotCreateUpdate extends Component {
    constructor(props){
        super(props);
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    componentDidMount(){
        const { match: { params } } =  this.props;
        if(params  &&  params.pk)
        {
            surfspotService.getSurfSpot(params.pk).then((c)=>{
                this.refs.name.value  =  c.name;
                this.refs.location.value  =  c.location;
                this.refs.buoyID.value  =  c.buoyID;
                this.refs.lastUpdated.value  =  c.lastUpdated;
            })
        }
    }
    handleSubmit(event) {
        const { match: { params } } =  this.props;
        if(params  &&  params.pk){
            this.handleUpdate(params.pk);
        }
        else
        {
            this.handleCreate();
        }
        event.preventDefault();
    }
    handleUpdate(pk){
        surfspotService.updateSurfSpot(
            {
            "pk":  pk,
            "name":  this.refs.name.value,
            "location":  this.refs.location.value,
            "buoyID":  this.refs.buoyID.value,
            }
            ).then((result)=>{
        
                alert("Surf spot updated!");
            }).catch(()=>{
                alert('There was an error! Please re-check your form.');
            });
        }
    handleCreate(){
        surfspotService.createSurfSpot(
            {
            "name":  this.refs.name.value,
            "location":  this.refs.location.value,
            "buoyID":  this.refs.buoyID.value,
            }).then((result)=>{
                    alert("Surf spot created!");
            }).catch(()=>{
                    alert('There was an error! Please re-check your form.');
            });
    }
    render() {
        return (
          <form onSubmit={this.handleSubmit}>
          <div className="form-group">
            <label>
              Name:</label>
              <input className="form-control" type="text" ref='name' />

            <label>
              Location:</label>
              <input className="form-control" type="text" ref='location'/>

            <label>
              Buoy ID:</label>
              <input className="form-control" type="text" ref='buoyID' />


            <input className="btn btn-primary" type="submit" value="Submit" />
            </div>
          </form>
        );
  }
}
export default SurfSpotCreateUpdate;