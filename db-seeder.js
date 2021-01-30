const faker = require("faker");
const Seeder = require("mysql-db-seed").Seeder;
// ES6 use `import {Seeder} from "mysql-db-seed";`

// Generate a new Seeder instance
const seed = new Seeder(
  10, 
  "localhost",
  "chris",
  "bd0nl@n",
  "as_db_security"
);

(async () => {
  await seed.seed(
    30,
    "table_one", 
    {
      name: faker.name.findName(),
      student_number: faker.random.uuid,
      date_of_birth: faker.date.past(),
      course: faker.random.word(),
      state: faker.address.state(),
      village: faker.address.county(),
      apartment: faker.random.number(),
      house: faker.address.streetName(),
      country: faker.address.country(),
      
    }
  )
  seed.exit();
  process.exit();
})();
