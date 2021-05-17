import React, { Component } from 'react';
import SurfSpotService from './SurfSpotService'


const surfspotService = new SurfSpotService();
class SurfSpotsList extends Component {
    constructor(props) {
        super(props);
        this.state = {
            surfspots: [],
            nextPageURL: ''
        };
        this.nextPage = this.nextPage.bind(this);
        this.handleDelete = this.handleDelete.bind(this);
    }
    componentDidMount() {
        var self = this;
        surfspotService.getSurfSpots().then((result) => 
            self.setState({surfspots: result.data, nextPageURL: result.nextlink}));
    }
    nextPage(){
        var self = this;
        surfspotService.getSurfSpotsByURL(this.state.nextPageURL).then((result)=>{
            self.setState({surfspots: result.data, nextPageURL: result.nextlink})
        });
    }
    handleDelete(e,pk) {
        var self = this;
        surfspotService.deleteSurfSpot({pk : pk}).then(()=>{
            var newArr = self.state.surfspots.filter((obj) =>{
                return obj.pk !== pk;
            });
            self.setState({surfspots: newArr})
        });
    }
    render() {
        return (
        <div className="surfspots--list">
            <table  className="table">
                <thead  key="thead">
                <tr>
                    <th>#</th>
                    <th>Surf Spot</th>
                    <th>Location</th>
                    <th>Buoy Data</th>
                    <th>Last Updated</th>
                </tr>
                </thead>
                <tbody>
                    {this.state.surfspots.map( c  =>
                    <tr  key={c.pk}>
                        <td>{c.pk}  </td>
                        <td>{c.name}</td>
                        <td>{c.location}</td>
                        <td>{c.buoyID}</td>
                        <td>{c.lastUpdated}</td>
                        <td>
                        <button  onClick={(e)=>  this.handleDelete(e,c.pk) }> Delete</button>
                        <a  href={"/surfspot/" + c.pk}> Update</a>
                        </td>
                    </tr>)}
                </tbody>
            </table>
            <button  className="btn btn-primary"  onClick=  {  this.nextPage  }>Next</button>
        </div>
        );
    }
}
export default SurfSpotsList;