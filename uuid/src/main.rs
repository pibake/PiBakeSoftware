extern crate uuid;

use std::io;
use std::io::Write;
use std::path::Path;
use uuid::Uuid;
use std::fs;
use std::fs::File;

fn main() {
    let mut my_uuid = Uuid::new_v4();
    println!("{}", my_uuid);
    write_to_txt(my_uuid);
}

fn write_to_txt(uuid :Uuid) -> io::Result<()> {
    let result = does_file_exist();

    if result == false {
        File::create("./uuid");
    } else {
        println!("File created!");
    }

    let uuid_string :String = uuid.to_string();

    fs::write("./uuid", uuid_string).expect("Unable to write file");

    println!("File written!");
    Ok(())
}

fn does_file_exist() -> bool {
    let result = Path::new("uuid").is_file();
    return result;
}