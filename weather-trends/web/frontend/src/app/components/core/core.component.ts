import { Component, OnInit } from '@angular/core';
import { FormGroup, Validators, FormControl } from '@angular/forms';
import { ApiService } from 'src/app/services/api.service';

@Component({
  selector: 'app-core',
  templateUrl: './core.component.html',
  styleUrls: ['./core.component.scss'],
})
export class CoreComponent implements OnInit {
  searchForm!: FormGroup;
  error: string = '';

  city: string = '';
  isLoading: boolean = false;
  isHaveChart: boolean = false;

  chartLink: string[] = [];

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.searchForm = new FormGroup({
      searchTerm: new FormControl(null, [Validators.required]),
    });
  }

  submitForm() {
    if (this.searchForm.valid) {
      let city = this.searchForm.getRawValue()['searchTerm'];
      this.isLoading = true;
      this.city = city;
      this.performSearch(city);
    } else {
      alert('City name is required!');
    }
  }
  performSearch(city: string) {
    this.apiService.getDataByCity(city).subscribe(
      (res: any) => {
        this.error = '';
        this.isHaveChart = true;
        this.isLoading = false;
        this.chartLink.push(
          'https://weather-trends-dand.herokuapp.com/' + res.file
        );
      },
      (err: any) => {
        this.isLoading = false;
        this.isHaveChart = false;

        if (err.status == 404) {
          this.error = 'Data with given city name is not found';
        }
      }
    );
  }
}
