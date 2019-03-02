extern crate uuid;

use std::fs;
use std::path::Path;
use uuid::Uuid;

fn main() {
    let my_uuid = Uuid::new_v4();
    println!("{}", my_uuid);
    write_to_txt(my_uuid);
}

fn write_to_txt(uuid :Uuid) {
    let result = does_file_exist();

    if result == false {
        fs::File::create("./uuid").expect("Unable to create file!");
        println!("File created!");
    } else {
        println!("File already created!");
    }

    let uuid_string :String = uuid.to_string();

    fs::write("./uuid", uuid_string).expect("Unable to write file");

    println!("File written!");
}

fn does_file_exist() -> bool {
    let result = Path::new("uuid").is_file();
    return result;
}